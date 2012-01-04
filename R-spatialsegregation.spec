%global packname  spatialsegregation
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.31
Release:          1%{?dist}
Summary:          Segregation measures for multitype spatial point patterns

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-spatstat 

BuildRequires:    R-devel tex(latex) R-spatstat 

%description
Summaries for measuring segregation/mingling in multitype spatial point
patterns with graph based neighbourhood description.  Included indices:
Mingling, Shannon, Simpson (also the non-spatial) Included functionals:
Mingling, Shannon, Simpson, ISAR, MCI.  Included neighbourhoods:
Geometric, k-nearest neighbours, Gabriel, Delaunay.

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
%doc %{rlibdir}/spatialsegregation/html
%doc %{rlibdir}/spatialsegregation/DESCRIPTION
%{rlibdir}/spatialsegregation/R
%{rlibdir}/spatialsegregation/INDEX
%{rlibdir}/spatialsegregation/help
RPM build errors:
%{rlibdir}/spatialsegregation/NAMESPACE
%{rlibdir}/spatialsegregation/Meta
%{rlibdir}/spatialsegregation/libs
%{rlibdir}/spatialsegregation/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.31-1
- initial package for Fedora