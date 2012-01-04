%global packname  PHYLOGR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Functions for phylogenetically based statistical analyses

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Manipulation and analysis of phylogenetically simulated data sets and
phylogenetically based analyses using GLS.

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
%doc %{rlibdir}/PHYLOGR/DESCRIPTION
%doc %{rlibdir}/PHYLOGR/html
%{rlibdir}/PHYLOGR/R
%{rlibdir}/PHYLOGR/NAMESPACE
%{rlibdir}/PHYLOGR/INDEX
%{rlibdir}/PHYLOGR/help
%{rlibdir}/PHYLOGR/Examples
%{rlibdir}/PHYLOGR/data
%{rlibdir}/PHYLOGR/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.7-1
- initial package for Fedora