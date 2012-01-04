%global packname  survcomp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Performance Assessment and Comparison for Survival Analysis

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-grid R-rmeta R-KernSmooth R-bootstrap R-survivalROC 
Requires:         R-ipred R-prodlim R-SuppDists R-KernSmooth 

BuildRequires:    R-devel tex(latex) R-survival R-grid R-rmeta R-KernSmooth R-bootstrap R-survivalROC
BuildRequires:    R-ipred R-prodlim R-SuppDists R-KernSmooth 


%description
R package providing functions to assess and to compare the performance of
risk prediction (survival) models.

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
%doc %{rlibdir}/survcomp/html
%doc %{rlibdir}/survcomp/DESCRIPTION
%doc %{rlibdir}/survcomp/CITATION
%doc %{rlibdir}/survcomp/doc
%{rlibdir}/survcomp/R
%{rlibdir}/survcomp/NAMESPACE
%{rlibdir}/survcomp/help
%{rlibdir}/survcomp/INDEX
%{rlibdir}/survcomp/Meta
%{rlibdir}/survcomp/libs
%{rlibdir}/survcomp/data

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora