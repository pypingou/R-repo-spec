%global packname  PAN
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Posterior association networks and functional modules inferred from rich phenotypes of gene perturbations

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-graphics R-grDevices R-igraph R-MASS R-methods R-pvclust R-stats R-utils 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-graphics R-grDevices R-igraph R-MASS R-methods R-pvclust R-stats R-utils 


%description
This package provides S4 classes and methods for inferring functional gene
networks with edges encoding posterior beliefs of gene association types
and nodes encoding perturbation effects.

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
%doc %{rlibdir}/PAN/NEWS
%doc %{rlibdir}/PAN/html
%doc %{rlibdir}/PAN/DESCRIPTION
%doc %{rlibdir}/PAN/doc
%{rlibdir}/PAN/data
%{rlibdir}/PAN/INDEX
%{rlibdir}/PAN/help
%{rlibdir}/PAN/Meta
%{rlibdir}/PAN/NAMESPACE
%{rlibdir}/PAN/R
%{rlibdir}/PAN/CHANGES

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora