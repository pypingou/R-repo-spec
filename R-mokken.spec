%global packname  mokken
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.6
Release:          1%{?dist}
Summary:          Mokken Scale Analysis in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
mokken contains functions for performing Mokken scale analysis on test and
questionnaire data. It includes an automated item selection algorithm, and
various checks of model assumptions.

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
%doc %{rlibdir}/mokken/html
%doc %{rlibdir}/mokken/DESCRIPTION
%doc %{rlibdir}/mokken/CITATION
%doc %{rlibdir}/mokken/doc
%{rlibdir}/mokken/help
%{rlibdir}/mokken/INDEX
%{rlibdir}/mokken/NAMESPACE
%{rlibdir}/mokken/Meta
%{rlibdir}/mokken/libs
%{rlibdir}/mokken/data
%{rlibdir}/mokken/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6-1
- initial package for Fedora