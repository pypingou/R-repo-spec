%global packname  BCBCSF
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          Bias-corrected Bayesian Classification with Selected Features

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-abind 

BuildRequires:    R-devel tex(latex) R-abind 

%description
This software is used to predict the discrete class labels based on a
selected subset of high-dimensional features, such as expression levels of
genes. The data are modeled with a hierarchical Bayesian models using
heavy-tailed t distributions as priors. When a large number of features
are available, one may like to select only a subset of features to use,
typically those features strongly correlated with the response in training
cases. Such a feature selection procedure is however invalid since the
relationship between the response and the features has be exaggerated by
feature selection. This package provides a way to avoid this bias and
yield better-calibrated predictions for future cases when one uses
F-statistic to select features.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora