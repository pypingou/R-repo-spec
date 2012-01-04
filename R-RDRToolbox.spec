%global packname  RDRToolbox
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          A package for nonlinear dimension reduction with Isomap and LLE.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rgl 
Requires:         R-graphics R-grDevices R-methods R-stats R-MASS R-rgl 

BuildRequires:    R-devel tex(latex) R-rgl
BuildRequires:    R-graphics R-grDevices R-methods R-stats R-MASS R-rgl 


%description
A package for nonlinear dimension reduction using the Isomap and LLE
algorithm. It also includes a routine for computing the
Davis-Bouldin-Index for cluster validation, a plotting tool and a data
generator for microarray gene expression data and for the Swiss Roll

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora