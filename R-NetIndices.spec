%global packname  NetIndices
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Estimating network indices, including trophic structure of foodwebs in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
Given a network (e.g. a food web), estimates several network indices.
These include: Ascendency network indices, Direct and indirect
dependencies, Effective measures, Environ network indices, General network
indices, Pathway analysis, Network uncertainty indices and constraint
efficiencies and the trophic level and omnivory indices of food webs.

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
%doc %{rlibdir}/NetIndices/html
%doc %{rlibdir}/NetIndices/DESCRIPTION
%doc %{rlibdir}/NetIndices/CITATION
%doc %{rlibdir}/NetIndices/doc
%{rlibdir}/NetIndices/Meta
%{rlibdir}/NetIndices/help
%{rlibdir}/NetIndices/EcologicalModelling
%{rlibdir}/NetIndices/R
%{rlibdir}/NetIndices/INDEX
%{rlibdir}/NetIndices/data
%{rlibdir}/NetIndices/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora