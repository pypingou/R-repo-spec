%global packname  rrcov
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.01
Release:          1%{?dist}
Summary:          Scalable Robust Estimators with High Breakdown Point

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-01.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-robustbase R-pcaPP R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-methods R-robustbase R-pcaPP R-mvtnorm 

%description
Robust Location and Scatter Estimation and Robust Multivariate Analysis
with High Breakdown Point.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.01-1
- initial package for Fedora