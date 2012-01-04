%global packname  predbayescor
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          Classification rule based on Bayesian naive Bayes models with feature selection bias corrected

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This software is used to predict the binary response based on high
dimensional features, for example gene expression data. The data are
modelled with Bayesian naive Bayes models. When a large number of features
are available, one may like to select only a subset of features to use,
typically those features strongly correlated with the response in training
cases. Such a feature selection procedure is however invalid since the
relationship between the response and the features will appear stronger.
This package provides a way to avoid this bias and yields well-calibrated
prediction for the test cases.

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
%doc %{rlibdir}/predbayescor/html
%doc %{rlibdir}/predbayescor/DESCRIPTION
%{rlibdir}/predbayescor/Meta
%{rlibdir}/predbayescor/INDEX
%{rlibdir}/predbayescor/help
%{rlibdir}/predbayescor/libs
%{rlibdir}/predbayescor/NAMESPACE
%{rlibdir}/predbayescor/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.4-1
- initial package for Fedora