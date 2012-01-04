%global packname  kohonen
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.7
Release:          1%{?dist}
Summary:          Supervised and unsupervised self-organising maps

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-class R-MASS 

BuildRequires:    R-devel tex(latex) R-class R-MASS 

%description
Supervised and unsupervised self-organising maps

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
%doc %{rlibdir}/kohonen/CITATION
%doc %{rlibdir}/kohonen/doc
%doc %{rlibdir}/kohonen/html
%doc %{rlibdir}/kohonen/DESCRIPTION
%{rlibdir}/kohonen/NAMESPACE
%{rlibdir}/kohonen/Meta
%{rlibdir}/kohonen/INDEX
%{rlibdir}/kohonen/R
%{rlibdir}/kohonen/libs
%{rlibdir}/kohonen/help
%{rlibdir}/kohonen/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.7-1
- initial package for Fedora