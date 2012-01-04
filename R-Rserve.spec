%global packname  Rserve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6.5
Release:          1%{?dist}
Summary:          Binary R server

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Rserve acts as a socket server (TCP/IP or local sockets) which allows
binary requests to be sent to R. Every connection has a separate workspace
and working directory. Client-side implementations are available for
popular languages such as C/C++ and Java, allowing any application to use
facilities of R without the need of linking to R code. Rserve supports
remote connection, user authentication and file transfer. A simple R
client is included in this package as well.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/Rserve/html
%doc %{rlibdir}/Rserve/NEWS
%doc %{rlibdir}/Rserve/DESCRIPTION
%{rlibdir}/Rserve/Rserve
%{rlibdir}/Rserve/R
%{rlibdir}/Rserve/libs
%{rlibdir}/Rserve/NAMESPACE
%{rlibdir}/Rserve/help
%{rlibdir}/Rserve/Rserve.dbg
%{rlibdir}/Rserve/Meta
%{rlibdir}/Rserve/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.5-1
- initial package for Fedora