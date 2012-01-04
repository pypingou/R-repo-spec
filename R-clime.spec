%global packname  clime
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Constrained L1-minimization for Inverse (covariance) Matrix Estimation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lpSolve 

BuildRequires:    R-devel tex(latex) R-lpSolve 

%description
A robust constrained L1 minimization method for estimating a large sparse
inverse covariance matrix (aka precision matrix), and recovering its
support for building graphical models.  The computation uses linear

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
%doc %{rlibdir}/clime/DESCRIPTION
%doc %{rlibdir}/clime/html
%{rlibdir}/clime/NAMESPACE
%{rlibdir}/clime/help
%{rlibdir}/clime/INDEX
%{rlibdir}/clime/R
%{rlibdir}/clime/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora