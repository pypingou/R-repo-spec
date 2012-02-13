%global packname  obsSens
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{dist}
Summary:          Sensitivity analysis for Observational studies.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Observational studies are limited in that there could be an unmeasured
variable related to both the response variable and the primary predictor. 
If this unmeasured variable were included in the analysis it would change
the relationship (possibly changing the conclusions).  Sensitivity
analysis is a way to see how much of a relationship needs to exist with
the unmeasured variable before the conclusions change.  This package
provides tools for doing a sensitivity analysis for regression (linear,
logistic, and cox) style models.

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
%doc %{rlibdir}/obsSens/html
%doc %{rlibdir}/obsSens/DESCRIPTION
%{rlibdir}/obsSens/R
%{rlibdir}/obsSens/NAMESPACE
%{rlibdir}/obsSens/help
%{rlibdir}/obsSens/INDEX
%{rlibdir}/obsSens/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- Update to version 1.2

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora