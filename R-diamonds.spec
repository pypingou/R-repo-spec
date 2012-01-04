%global packname  diamonds
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Analysis and sampling grids from diamond partitions

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions for illustrating aperture-4 diamond partitions in the plane, or
on the surface of an octahedron or icosahedron, for use as analysis or
sampling grids.

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
%doc %{rlibdir}/diamonds/html
%doc %{rlibdir}/diamonds/DESCRIPTION
%{rlibdir}/diamonds/R
%{rlibdir}/diamonds/NAMESPACE
%{rlibdir}/diamonds/help
%{rlibdir}/diamonds/INDEX
%{rlibdir}/diamonds/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora