%global packname  MLEcens
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Computation of the MLE for bivariate (interval) censored data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains functions to compute the nonparametric maximum
likelihood estimator (MLE) for the bivariate distribution of (X,Y), when
realizations of (X,Y) cannot be observed directly. To be more precise, we
consider the situation where we observe a set of rectangles (that we call
'observation rectangles') that are known to contain the unobservable
realizations of (X,Y). We compute the MLE based on such a set of
rectangles. The methods can also be used for univariate censored data (see
data set 'cosmesis'), and for censored data with competing risks (see data
set 'menopause'). We also provide functions to visualize the observed data
and the MLE. (This package contains the functionality of the R-package
'bicreduc', which will no longer be maintained.)

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
%doc %{rlibdir}/MLEcens/html
%doc %{rlibdir}/MLEcens/DESCRIPTION
%{rlibdir}/MLEcens/data
%{rlibdir}/MLEcens/libs
%{rlibdir}/MLEcens/Meta
%{rlibdir}/MLEcens/R
%{rlibdir}/MLEcens/NAMESPACE
%{rlibdir}/MLEcens/INDEX
%{rlibdir}/MLEcens/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora