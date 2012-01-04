%global packname  LogicForest
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.0
Release:          1%{?dist}
Summary:          Logic Forest

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-LogicReg R-CircStats R-gtools R-plotrix 

BuildRequires:    R-devel tex(latex) R-LogicReg R-CircStats R-gtools R-plotrix 

%description
Two classification ensemble methods based on logic regression models. 
Logforest uses a bagging approach to contruct an ensemble of logic
regression models.  LBoost uses a combination of boosting and
cross-validation to construct and ensemble of logic regression models. 
Both methods are used for classification of binary responses based on
binary predictors and for identification of important variables and
variable interactions predictive of a binary outcome.

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
%doc %{rlibdir}/LogicForest/html
%doc %{rlibdir}/LogicForest/DESCRIPTION
%{rlibdir}/LogicForest/INDEX
%{rlibdir}/LogicForest/help
%{rlibdir}/LogicForest/data
%{rlibdir}/LogicForest/Meta
%{rlibdir}/LogicForest/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.0-1
- initial package for Fedora