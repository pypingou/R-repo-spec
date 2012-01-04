%global packname  sddpack
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          Semidiscrete Decomposition

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The semidiscrete decomposition (SDD) approximates a matrix as a weighted
sum of outer products formed by vectors with entries constrained to be in
the set {-1, 0, 1}.

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
%doc %{rlibdir}/sddpack/DESCRIPTION
%doc %{rlibdir}/sddpack/html
%{rlibdir}/sddpack/NAMESPACE
%{rlibdir}/sddpack/Meta
%{rlibdir}/sddpack/help
%{rlibdir}/sddpack/INDEX
%{rlibdir}/sddpack/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora