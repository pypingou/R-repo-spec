%global packname  abind
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.0
Release:          1%{?dist}
Summary:          Combine multi-dimensional arrays

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Combine multi-dimensional arrays into a single array. This is a
generalization of cbind and rbind.  Works with vectors, matrices, and
higher-dimensional arrays.  Also provides functions adrop, asub, and afill
for manipulating, extracting and replacing data in arrays.

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
%doc %{rlibdir}/abind/DESCRIPTION
%doc %{rlibdir}/abind/html
%{rlibdir}/abind/INDEX
%{rlibdir}/abind/R
%{rlibdir}/abind/Meta
%{rlibdir}/abind/NAMESPACE
%{rlibdir}/abind/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.0-1
- initial package for Fedora