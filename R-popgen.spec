%global packname  popgen
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Statistical and Population Genetics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster 

BuildRequires:    R-devel tex(latex) R-cluster 

%description
A package that implements a variety of statistical and population genetic

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
%doc %{rlibdir}/popgen/DESCRIPTION
%doc %{rlibdir}/popgen/html
%{rlibdir}/popgen/NAMESPACE
%{rlibdir}/popgen/R
%{rlibdir}/popgen/INDEX
%{rlibdir}/popgen/example_data1
%{rlibdir}/popgen/example_data2
%{rlibdir}/popgen/help
%{rlibdir}/popgen/README
%{rlibdir}/popgen/libs
%{rlibdir}/popgen/Meta
%{rlibdir}/popgen/HISTORY

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora