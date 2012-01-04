%global packname  np
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.40.11
Release:          1%{?dist}
Summary:          Nonparametric kernel smoothing methods for mixed data types

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.40-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot R-cubature 

BuildRequires:    R-devel tex(latex) R-boot R-cubature 

%description
This package provides a variety of nonparametric (and semiparametric)
kernel methods that seamlessly handle a mix of continuous, unordered, and
ordered factor data types. We would like to gratefully acknowledge support
from the Natural Sciences and Engineering Research Council of Canada
(NSERC:www.nserc.ca), the Social Sciences and Humanities Research Council
of Canada (SSHRC:www.sshrc.ca), and the Shared Hierarchical Academic
Research Computing Network (SHARCNET:www.sharcnet.ca).

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.40.11-1
- initial package for Fedora