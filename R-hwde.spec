%global packname  hwde
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.62
Release:          1%{?dist}
Summary:          Models and tests for departure from Hardy-Weinberg equilibrium and independence between loci.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Fits models for genotypic disequilibria, as described in Huttley and
Wilson (2000), Weir (1996) and Weir and Wilson (1986). Contrast terms are
available that account for first order interactions between loci. Also
implements, for a single locus in a single population, a conditional exact
test for Hardy-Weinberg equilibrium

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
%doc %{rlibdir}/hwde/DESCRIPTION
%doc %{rlibdir}/hwde/doc
%doc %{rlibdir}/hwde/html
%{rlibdir}/hwde/help
%{rlibdir}/hwde/INDEX
%{rlibdir}/hwde/Meta
%{rlibdir}/hwde/data
%{rlibdir}/hwde/R
%{rlibdir}/hwde/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.62-1
- initial package for Fedora