%global packname  aws
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.2
Release:          1%{?dist}
Summary:          Adaptive Weights Smoothing

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.6-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
The package contains R-functions implementing the Propagation-Separation
Approach to adaptive smoothing as described in J. Polzehl and V. Spokoiny
(2006), Propagation-Separation Approach for Local Likelihood Estimation,
Prob. Theory and Rel. Fields, 135(3):335--362. and J. Polzehl and V.
Spokoiny (2004) Spatially adaptive regression estimation:
Propagation-separation approach, WIAS-Preprint 998.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.2-1
- initial package for Fedora