%global packname  ChemometricsWithR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{dist}
Summary:          Chemometrics with R - Multivariate Data Analysis in the Natural Sciences and Life Sciences

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-ChemometricsWithRData R-MASS R-nnet R-randomForest R-ada R-rrcov R-sfsmisc R-ipred R-fastICA R-rda R-TIMP R-class R-e1071 R-rpart R-cluster R-msProstate R-ALS R-ptw R-dtw R-boot R-leaps R-lars R-elasticnet R-subselect R-kohonen R-pls R-signal R-mclust 


BuildRequires:    R-devel tex(latex) R-ChemometricsWithRData R-MASS R-nnet R-randomForest R-ada R-rrcov R-sfsmisc R-ipred R-fastICA R-rda R-TIMP R-class R-e1071 R-rpart R-cluster R-msProstate R-ALS R-ptw R-dtw R-boot R-leaps R-lars R-elasticnet R-subselect R-kohonen R-pls R-signal R-mclust



%description
The package provides functions and scripts used in the book "Chemometrics
with R - Multivariate Data Analysis in the Natural Sciences and Life
Sciences" by Ron Wehrens, Springer (2011).

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
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- Update to version 0.1.5

* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora