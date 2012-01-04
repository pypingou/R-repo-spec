%global packname  rfPermute
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Estimate permutation p-values for importance metrics.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-randomForest 

BuildRequires:    R-devel tex(latex) R-randomForest 

%description
Estimate significance of importance metrics for a Random Forest model by
permuting the response variable. Produces null distribution of importance
metrics for each predictor variable and p-value of observed.

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
%doc %{rlibdir}/rfPermute/html
%doc %{rlibdir}/rfPermute/DESCRIPTION
%{rlibdir}/rfPermute/help
%{rlibdir}/rfPermute/INDEX
%{rlibdir}/rfPermute/Meta
%{rlibdir}/rfPermute/NAMESPACE
%{rlibdir}/rfPermute/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora