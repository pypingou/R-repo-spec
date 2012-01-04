%global packname  SMIR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.02
Release:          1%{?dist}
Summary:          Companion to Statistical Modelling in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package accompanies Aitkin et al, Statistical Modelling in R, OUP,
2009. The package contains some functions and datasets used in the text.

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
%doc %{rlibdir}/SMIR/html
%doc %{rlibdir}/SMIR/DESCRIPTION
%{rlibdir}/SMIR/Meta
%{rlibdir}/SMIR/NAMESPACE
%{rlibdir}/SMIR/data
%{rlibdir}/SMIR/INDEX
%{rlibdir}/SMIR/R
%{rlibdir}/SMIR/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.02-1
- initial package for Fedora