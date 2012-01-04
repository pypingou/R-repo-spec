%global packname  constrainedKriging
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.6
Release:          1%{?dist}
Summary:          Constrained, covariance-matching constrained and universal point or block kriging

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-sp R-spatialCovariance R-methods 
Requires:         R-gpclib R-RandomFields 

BuildRequires:    R-devel tex(latex) R-sp R-spatialCovariance R-methods
BuildRequires:    R-gpclib R-RandomFields 


%description
The constrainedKriging package provides functions for efficient
computations of nonlinear spatial predictions with local change of
support. The package supplies functions for two-dimensional spatial
interpolation by constrained, covariance-matching constrained and
universal (external drift) kriging for points or block of any shape for
data with a nonstationary mean function and an isotropic weakly stationary
variogram. The linear spatial interpolation methods, constrained and
covariance-matching constrained kriging, provide approximately unbiased
prediction for nonlinear target values under change of support. The
constrainedKriging package extends the range of geostatistical tools
available in R and provides a veritable alternative to conditional
simulation for nonlinear spatial prediction problems with local change of

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
%doc %{rlibdir}/constrainedKriging/doc
%doc %{rlibdir}/constrainedKriging/CITATION
%doc %{rlibdir}/constrainedKriging/DESCRIPTION
%doc %{rlibdir}/constrainedKriging/LICENCE
%doc %{rlibdir}/constrainedKriging/html
%{rlibdir}/constrainedKriging/Meta
%{rlibdir}/constrainedKriging/help
%{rlibdir}/constrainedKriging/libs
%{rlibdir}/constrainedKriging/data
%{rlibdir}/constrainedKriging/R
%{rlibdir}/constrainedKriging/ChangeLog.txt
%{rlibdir}/constrainedKriging/NAMESPACE
%{rlibdir}/constrainedKriging/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.6-1
- initial package for Fedora