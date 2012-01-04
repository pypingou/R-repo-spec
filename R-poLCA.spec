%global packname  poLCA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Polytomous variable Latent Class Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-scatterplot3d R-MASS 

BuildRequires:    R-devel tex(latex) R-scatterplot3d R-MASS 

%description
Latent class analysis and latent class regression models for polytomous
outcome variables.  Also known as latent structure analysis.

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
%doc %{rlibdir}/poLCA/doc
%doc %{rlibdir}/poLCA/DESCRIPTION
%doc %{rlibdir}/poLCA/html
%doc %{rlibdir}/poLCA/CITATION
%{rlibdir}/poLCA/data
%{rlibdir}/poLCA/libs
%{rlibdir}/poLCA/Meta
%{rlibdir}/poLCA/NAMESPACE
%{rlibdir}/poLCA/R
%{rlibdir}/poLCA/INDEX
%{rlibdir}/poLCA/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora