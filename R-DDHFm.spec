%global packname  DDHFm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3.1
Release:          1%{?dist}
Summary:          Variance Stabilization by Data-Driven Haar-Fisz (for Microarrays)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package contains the normalizing and variance stabilizing Data-Driven
Haar-Fisz algorithm. Also contains related algorithms for simulating from
certain microarray gene intensity models and evaluation of certain

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
%doc %{rlibdir}/DDHFm/doc
%doc %{rlibdir}/DDHFm/DESCRIPTION
%doc %{rlibdir}/DDHFm/html
%{rlibdir}/DDHFm/help
%{rlibdir}/DDHFm/R
%{rlibdir}/DDHFm/INDEX
%{rlibdir}/DDHFm/NAMESPACE
%{rlibdir}/DDHFm/libs
%{rlibdir}/DDHFm/data
%{rlibdir}/DDHFm/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3.1-1
- initial package for Fedora