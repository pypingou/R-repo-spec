%global packname  rsae
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Robust Small Area Estimation

Group:            Applications/Engineering 
License:          GPL (>= 2) | FreeBSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Robust Small Area Estimation. Robust Basic Unit- and Area-Level Models

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
%doc %{rlibdir}/rsae/CITATION
%doc %{rlibdir}/rsae/html
%doc %{rlibdir}/rsae/doc
%doc %{rlibdir}/rsae/DESCRIPTION
%{rlibdir}/rsae/R
%{rlibdir}/rsae/help
%{rlibdir}/rsae/INDEX
%{rlibdir}/rsae/NAMESPACE
%{rlibdir}/rsae/libs
%{rlibdir}/rsae/data
%{rlibdir}/rsae/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora