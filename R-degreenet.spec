%global packname  degreenet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Models for Skewed Count Distributions Relevant to Networks

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Likelihood-based inference for skewed count distributions used in network
modeling. "degreenet" is a part of the "statnet" suite of packages for
network analysis.  For a list of functions type: help(package='degreenet')

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
%doc %{rlibdir}/degreenet/DESCRIPTION
%doc %{rlibdir}/degreenet/CITATION
%doc %{rlibdir}/degreenet/html
%{rlibdir}/degreenet/libs
%{rlibdir}/degreenet/flo.paj
%{rlibdir}/degreenet/data
%{rlibdir}/degreenet/floadj.txt
%{rlibdir}/degreenet/R
%{rlibdir}/degreenet/Meta
%{rlibdir}/degreenet/help
%{rlibdir}/degreenet/LICENSE
%{rlibdir}/degreenet/INDEX
RPM build errors:
%{rlibdir}/degreenet/demo
%{rlibdir}/degreenet/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora