%global packname  expm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.98.5
Release:          1%{?dist}
Summary:          Matrix exponential

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.98-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-Matrix 

%description
Computation of the matrix exponential and related quantities.

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
%doc %{rlibdir}/expm/DESCRIPTION
%doc %{rlibdir}/expm/doc
%doc %{rlibdir}/expm/html
%{rlibdir}/expm/NAMESPACE
%{rlibdir}/expm/demo
%{rlibdir}/expm/libs
%{rlibdir}/expm/Meta
%{rlibdir}/expm/R
%{rlibdir}/expm/test-tools.R
%{rlibdir}/expm/po
%{rlibdir}/expm/help
%{rlibdir}/expm/INDEX
%{rlibdir}/expm/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.98.5-1
- initial package for Fedora