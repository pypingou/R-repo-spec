%global packname  profdpm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.0
Release:          1%{?dist}
Summary:          Profile Dirichlet Process Mixtures

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package facilitates profile inference (inference at the posterior
mode) for a class of product partition models (PPM). The Dirichlet process
mixture is currently the only available member of this class. These
methods search for the maximum posterior (MAP) estimate for the data
partition in a PPM.

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
%doc %{rlibdir}/profdpm/DESCRIPTION
%doc %{rlibdir}/profdpm/doc
%doc %{rlibdir}/profdpm/html
%{rlibdir}/profdpm/R
%{rlibdir}/profdpm/libs
%{rlibdir}/profdpm/NAMESPACE
%{rlibdir}/profdpm/INDEX
%{rlibdir}/profdpm/Meta
%{rlibdir}/profdpm/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.0-1
- initial package for Fedora