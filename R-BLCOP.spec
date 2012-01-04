%global packname  BLCOP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          Black-Litterman and copula-opinion pooling frameworks

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-MASS R-quadprog 

BuildRequires:    R-devel tex(latex) R-methods R-MASS R-quadprog 

%description
An implementation of the Black-Litterman Model and Atilio Meucci's copula
opinion pooling framework.  This should be regarded as a beta release.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.6-1
- initial package for Fedora