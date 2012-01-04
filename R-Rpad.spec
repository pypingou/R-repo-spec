%global packname  Rpad
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Workbook-style, web-based interface to R

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-utils R-grDevices 

BuildRequires:    R-devel tex(latex) R-graphics R-utils R-grDevices 

%description
A workbook-style user interface to R through a web browser. Provides
convenient plotting, HTML GUI generation, and HTML output routines. Can be
used with R in standalone mode or with a webserver to serve Rpad pages to
other users.

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
%doc %{rlibdir}/Rpad/html
%doc %{rlibdir}/Rpad/DESCRIPTION
%{rlibdir}/Rpad/basehtml
%{rlibdir}/Rpad/serverversion
%{rlibdir}/Rpad/Meta
/usr
%{rlibdir}/Rpad/INDEX
%{rlibdir}/Rpad/R
%{rlibdir}/Rpad/help
%{rlibdir}/Rpad/ChangeLog
%{rlibdir}/Rpad/localversion
%{rlibdir}/Rpad/NAMESPACE
RPM build errors:
%{rlibdir}/Rpad/tcl

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.0-1
- initial package for Fedora