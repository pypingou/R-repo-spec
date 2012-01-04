%global packname  nncRda
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.87
Release:          1%{?dist}
Summary:          Improved RDA Using nnc

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nnc R-rda R-MASS 

BuildRequires:    R-devel tex(latex) R-nnc R-rda R-MASS 

%description
Improved RDA (Regularized discriminant analysis) for class prediction in
microarrays using nearest neighbour covariates.

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
%doc %{rlibdir}/nncRda/DESCRIPTION
%doc %{rlibdir}/nncRda/html
%{rlibdir}/nncRda/NAMESPACE
%{rlibdir}/nncRda/R
%{rlibdir}/nncRda/Meta
%{rlibdir}/nncRda/help
%{rlibdir}/nncRda/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.87-1
- initial package for Fedora