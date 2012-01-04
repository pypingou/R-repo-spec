%global packname  mmcm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Modified Maximum Contrast Method

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This package provides an implementation of modified maximum contrast
methods and the maximum contrast method. This version supports functions
mmcm.mvt, mcm.mvt that gives P-value by using randomized quasi-Monte Carlo
method from pmvt function of package mvtnorm, and mmcm.resamp that gives
P-value by using the permutation method.

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
%doc %{rlibdir}/mmcm/CITATION
%doc %{rlibdir}/mmcm/DESCRIPTION
%doc %{rlibdir}/mmcm/html
%doc %{rlibdir}/mmcm/NEWS
%{rlibdir}/mmcm/R
%{rlibdir}/mmcm/help
%{rlibdir}/mmcm/INDEX
%{rlibdir}/mmcm/libs
%{rlibdir}/mmcm/NAMESPACE
RPM build errors:
%{rlibdir}/mmcm/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora