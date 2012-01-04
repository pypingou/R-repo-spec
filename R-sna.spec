%global packname  sna
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Tools for Social Network Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
A range of tools for social network analysis, including node and
graph-level indices, structural distance and covariance methods,
structural equivalence detection, p* modeling, random graph generation,
and 2D/3D network visualization.

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
%doc %{rlibdir}/sna/html
%doc %{rlibdir}/sna/DESCRIPTION
%{rlibdir}/sna/data
%{rlibdir}/sna/INDEX
%{rlibdir}/sna/R
%{rlibdir}/sna/NAMESPACE
%{rlibdir}/sna/libs
RPM build errors:
%{rlibdir}/sna/help
%{rlibdir}/sna/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.0-1
- initial package for Fedora