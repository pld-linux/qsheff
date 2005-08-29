# TODO
# - QMAILQUEUE integration
Summary:	qSheff - qmail queue wrapper
Summary(pl):	qSheff - wrapper dla kolejki qmaila
Name:		qsheff
%define	_ver 1.0
%define	_rel 3
Version:	%{_ver}.%{_rel}
Release:	0.6
Epoch:		0
License:	GPL v2
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/qsheff/%{name}-%{_ver}-r%{_rel}.tar.gz
# Source0-md5:	8b38b725c4ebf38764d4660d87d67391
Patch0:		%{name}-am.patch
URL:		http://www.enderunix.org/qsheff/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ripmime
Requires:	qmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not FHS compliant
%define		varqmail	/var/qmail

%description
qSheff is a wrapper for the qmail queue that scans email for viruses
and spam. Infected messages are rejected before they reach the queue,
so the server doesn't perform any job for them. After checking the
message, it will wake the qmail queue.

%description -l pl
qSheff to wrapper dla kolejki wmaila skanuj±cy pocztê pod k±tem
wirusów i spamu. Zainfekowane wiadomo¶ci s± odrzucane zanim wejd± do
kolejki, wiêc serwer nie wykona na nich ¿adnej pracy. Po sprawdzeniu
wiadomo¶ci zostanie ona umieszczona w kolejce.

%prep
%setup -q -n %{name}-%{_ver}-r%{_rel}
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	%{?debug:--enable-debug} \
	--bindir=%{_sbindir} \
	--with-qmaildir=%{varqmail} \
	--with-qmailgroup=qmail \
	--with-max-wordcount=1024

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_sysconfdir}/qsheff/{*install*.sh,*-default}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README THANKS TODO UPGRADE
%doc contribute/spamass-qsheff.en.html
%doc share/{developer.notes,*.{msg,txt}}
%attr(755,root,root) %{_sbindir}/qsheff
%attr(755,root,root) %{varqmail}/bin/qmail-qsheff
%dir %{_sysconfdir}/qsheff
%{_sysconfdir}/qsheff/qsheff.attach
%{_sysconfdir}/qsheff/qsheff.conf
%{_sysconfdir}/qsheff/qsheff.rules
%{_sysconfdir}/qsheff/qsheff.wblist
