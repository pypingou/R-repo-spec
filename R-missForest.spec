%global packname  missForest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Nonparametric Missing Value Imputation using Random Forest

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-randomForest 

BuildRequires:    R-devel tex(latex) R-randomForest 

%description
The function 'missForest' in this package is used to impute missing values
particularly in the case of mixed-type data. It uses a random forest
trained on the observed values of a data matrix to predict the missing
values. It can be used to impute continuous and/or categorical data
including complex interactions and nonlinear relations. It yields an
out-of-bag (OOB) imputation error estimate without the need of a test set
or elaborate cross-validation.

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
%doc %{rlibdir}/missForest/DESCRIPTION
%doc %{rlibdir}/missForest/doc
%doc %{rlibdir}/missForest/html
%{rlibdir}/missForest/INDEX
%{rlibdir}/missForest/Meta
%{rlibdir}/missForest/NAMESPACE
%{rlibdir}/missForest/help
%{rlibdir}/missForest/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora