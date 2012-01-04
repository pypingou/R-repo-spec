%global packname  MMG
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Mixture Model on Graphs

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package implements the Mixture Model on Graphs developed in
Sanguinetti et al., Bioinformatics 2008.  The graph structure is used to
infer quantities that were not measured, based on the neighbours'
measurements.  This approach was developed to address problems typical of
Quantitative Proteomics but could be applicable to many other domains.

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
%doc %{rlibdir}/MMG/DESCRIPTION
%doc %{rlibdir}/MMG/doc
%doc %{rlibdir}/MMG/html
%{rlibdir}/MMG/Meta
%{rlibdir}/MMG/help
%{rlibdir}/MMG/libs
%{rlibdir}/MMG/R
%{rlibdir}/MMG/NAMESPACE
%{rlibdir}/MMG/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora