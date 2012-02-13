%global packname  mvmeta
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.4
Release:          1%{dist}
Summary:          Multivariate meta-analysis and meta-regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package mvmeta contains functions to run fixed and random effects
meta-analysis and meta-regression on multiple outcomes.

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
%doc %{rlibdir}/mvmeta/html
%doc %{rlibdir}/mvmeta/DESCRIPTION
%doc %{rlibdir}/mvmeta/CITATION
%{rlibdir}/mvmeta/R
%{rlibdir}/mvmeta/INDEX
%{rlibdir}/mvmeta/ChangeLog
%{rlibdir}/mvmeta/help
%{rlibdir}/mvmeta/data
%{rlibdir}/mvmeta/NAMESPACE
%{rlibdir}/mvmeta/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.4-1
- Update to version 0.2.4

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.3-1
- initial package for Fedora