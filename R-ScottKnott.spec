%global packname  ScottKnott
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          The ScottKnott Clustering Algoritm

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-base 

BuildRequires:    R-devel tex(latex) R-stats R-base 

%description
Division of an ANOVA experiment treatment means into homogeneous distinct
groups using the clustering method of Scott & Knott

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
%doc %{rlibdir}/ScottKnott/DESCRIPTION
%doc %{rlibdir}/ScottKnott/html
%doc %{rlibdir}/ScottKnott/CITATION
%{rlibdir}/ScottKnott/help
%{rlibdir}/ScottKnott/Meta
%{rlibdir}/ScottKnott/INDEX
%{rlibdir}/ScottKnott/data
%{rlibdir}/ScottKnott/R
%{rlibdir}/ScottKnott/NAMESPACE
%{rlibdir}/ScottKnott/demo

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora