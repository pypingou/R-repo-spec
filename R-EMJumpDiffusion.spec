%global packname  EMJumpDiffusion
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          EM-Algorithm for Jump Diffusion processes

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Calculates parameters for Jump Diffusion processes via EM-Algorithm. The
jumps-times are considered to be bernoulli distributed with normally
distributed jump-sizes.

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
%doc %{rlibdir}/EMJumpDiffusion/DESCRIPTION
%doc %{rlibdir}/EMJumpDiffusion/html
%{rlibdir}/EMJumpDiffusion/help
%{rlibdir}/EMJumpDiffusion/Meta
%{rlibdir}/EMJumpDiffusion/R
%{rlibdir}/EMJumpDiffusion/INDEX
%{rlibdir}/EMJumpDiffusion/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.1-1
- initial package for Fedora