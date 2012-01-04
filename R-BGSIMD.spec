%global packname  BGSIMD
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Block Gibbs Sampler with Incomplete Multinomial Distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Implement an efficient block Gibbs sampler with incomplete data from a
multinomial distribution taking values from the k categories 1,2,...,k,
where data are assumed to miss at random and each missing datum belongs to
one and only one of m distinct non-empty proper subsets A1, A2,..., Am of
1,2,...,k and the k categories are labelled such that only consecutive A's
may overlap.

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
%doc %{rlibdir}/BGSIMD/DESCRIPTION
%doc %{rlibdir}/BGSIMD/html
%{rlibdir}/BGSIMD/Meta
%{rlibdir}/BGSIMD/INDEX
%{rlibdir}/BGSIMD/help
%{rlibdir}/BGSIMD/NAMESPACE
%{rlibdir}/BGSIMD/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora