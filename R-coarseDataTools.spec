%global packname  coarseDataTools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          A collection of functions to help with analysis of coarse infectious disease data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
This package contains functions to analyze coarse data. Its development
was motivated by applications to infectious disease: in particular,
problems with estimating the incubation period and the case fatality ratio
of a given disease.  Sample data files are included in the package.

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
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.1-1
- initial package for Fedora