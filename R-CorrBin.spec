%global packname  CorrBin
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.02
Release:          1%{?dist}
Summary:          Nonparametrics with clustered binary data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot 

BuildRequires:    R-devel tex(latex) R-boot 

%description
This package implements non-parametric analyses for clustered binary data.
The elements of the cluster are assumed exchangeable, and identical joint
distribution (also known as marginal compatibility, or reproducibility) is
assumed for clusters of different sizes. A trend test based on stochastic
ordering is implemented.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.02-1
- initial package for Fedora