%global packname  gptk
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.04
Release:          1%{?dist}
Summary:          Gaussian Processes Tool-Kit

Group:            Applications/Engineering 
License:          AGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-fields R-Matrix 

BuildRequires:    R-devel tex(latex) R-fields R-Matrix 

%description
The gptk package implements a general-purpose toolkit for Gaussian process
regression with a variety of covariance functions (e.g. RBF, Mattern,
polynomial, etc). Based on a MATLAB implementation by Neil D. Lawrence.
See inst/doc/index.html for more details.

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
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.04-1
- initial package for Fedora