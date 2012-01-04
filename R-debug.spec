%global packname  debug
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.40
Release:          1%{?dist}
Summary:          MVB's debugger for R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-mvbutils R-tcltk 

BuildRequires:    R-devel tex(latex) R-mvbutils R-tcltk 

%description
Debugger for R functions, with code display, graceful error recovery,
line-numbered conditional breakpoints, access to exit code, flow control,
and full keyboard input.

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
%doc %{rlibdir}/debug/html
%doc %{rlibdir}/debug/DESCRIPTION
%{rlibdir}/debug/R
%{rlibdir}/debug/Meta
%{rlibdir}/debug/help
%{rlibdir}/debug/NAMESPACE
%{rlibdir}/debug/changes.txt
%{rlibdir}/debug/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.40-1
- initial package for Fedora