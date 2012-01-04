%global packname  HardyWeinberg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Graphical tests for Hardy-Weinberg equilibrium

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-graphics R-stats 

%description
Package HardyWeinberg is a package for exploring bi-allelic marker data.
It focuses on the graphical representation of the results of tests for
Hardy-Weinberg equlibrium in a ternary plot. Routines for several tests
for Hardy-Weinberg equilibrium are included in the package.

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
%doc %{rlibdir}/HardyWeinberg/doc
%doc %{rlibdir}/HardyWeinberg/DESCRIPTION
%doc %{rlibdir}/HardyWeinberg/html
%{rlibdir}/HardyWeinberg/INDEX
%{rlibdir}/HardyWeinberg/Meta
%{rlibdir}/HardyWeinberg/R
%{rlibdir}/HardyWeinberg/help
%{rlibdir}/HardyWeinberg/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora