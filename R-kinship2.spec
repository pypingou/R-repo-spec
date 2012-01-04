%global packname  kinship2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Pedigree functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix R-quadprog 

BuildRequires:    R-devel tex(latex) R-Matrix R-quadprog 

%description
Routines to handle family data with a pedigree object. The initial purpose
was to create correlation structures that describe family relationships
such as kinship and identity-by-descent, which can be used to model family
data in mixed effects models, such as in the coxme function.  Also
includes a tool for pedigree drawing which is focused on producing compact
layouts without intervention.  Recent additions include utilities to trim
the pedigree object with various criteria.

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
%doc %{rlibdir}/kinship2/html
%doc %{rlibdir}/kinship2/doc
%doc %{rlibdir}/kinship2/DESCRIPTION
%{rlibdir}/kinship2/data
%{rlibdir}/kinship2/R
%{rlibdir}/kinship2/COPYRIGHT
%{rlibdir}/kinship2/help
%{rlibdir}/kinship2/INDEX
%{rlibdir}/kinship2/NEWS.Rd
%{rlibdir}/kinship2/Meta
%{rlibdir}/kinship2/NAMESPACE
%{rlibdir}/kinship2/GPL2.txt

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora