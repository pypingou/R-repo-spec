%global packname  indicspecies
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{dist}
Summary:          Functions to assess the strength and significance of relationship of species site group associations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides a set of functions to assess the strength of species
site group associations. It is also possible to check the statistical
significance of such associations.

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
%doc %{rlibdir}/indicspecies/html
%doc %{rlibdir}/indicspecies/DESCRIPTION
%doc %{rlibdir}/indicspecies/CITATION
%{rlibdir}/indicspecies/INDEX
%{rlibdir}/indicspecies/R
%{rlibdir}/indicspecies/help
%{rlibdir}/indicspecies/Meta
%{rlibdir}/indicspecies/NAMESPACE
%{rlibdir}/indicspecies/data

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- Update to version 1.6.0

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.2-1
- initial package for Fedora