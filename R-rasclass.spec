%global packname  rasclass
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Supervised Raster Image Classification

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-methods R-car R-nnet R-RSNNS R-e1071 R-randomForest 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-methods R-car R-nnet R-RSNNS R-e1071 R-randomForest 


%description
This package contains functions to perform supervised and pixel based
raster image classification. It has been designed to facilitate land-cover
analysis. Five classification algorithms can be used: Maximum Likelihood
Classification, Multinomial Logistic Regression, Neural Networks, Random
Forests and Support Vector Machines. The output includes the classified
raster and standard classification accuracy assessment (accuracy matrix,
overall accuracy and kappa coefficient). An option for in-sample
verification is available.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora