%global packname  clv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Cluster Validation Techniques

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster R-class 

BuildRequires:    R-devel tex(latex) R-cluster R-class 

%description
Package contains most of the popular internal and external cluster
validation methods ready to use for the most of the outputs produced by
functions coming from package "cluster". Package contains also functions
and examples of usage for cluster stability approach that might be applied
to algorithms implemented in "cluster" package as well as user defined
clustering algorithms.

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
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.2-1
- initial package for Fedora