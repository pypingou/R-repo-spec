%global packname  CVThresh
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Level-Dependent Cross-Validation Thresholding

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-wavethresh R-EbayesThresh 

BuildRequires:    R-devel tex(latex) R-wavethresh R-EbayesThresh 

%description
This package carries out level-dependent cross-validation method for the
selection of thresholding value in wavelet shrinkage. This procedure is
implemented by coupling a conventional cross validation with an imputation
method due to a limitation of data length, a power of 2. It can be easily
applied to classical leave-one-out and k-fold cross validation. Since the
procedure is computationally fast, a level-dependent cross validation can
be performed for wavelet shrinkage of various data such as a data with
correlated errors.

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
%doc %{rlibdir}/CVThresh/html
%doc %{rlibdir}/CVThresh/DESCRIPTION
%{rlibdir}/CVThresh/data
%{rlibdir}/CVThresh/help
%{rlibdir}/CVThresh/Meta
%{rlibdir}/CVThresh/INDEX
%{rlibdir}/CVThresh/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora