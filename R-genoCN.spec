%global packname  genoCN
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          genotyping and copy number study tools

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Simultaneous identification of copy number states and genotype calls for
regions of either copy number variations or copy number aberrations

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
%doc %{rlibdir}/genoCN/DESCRIPTION
%doc %{rlibdir}/genoCN/NEWS
%doc %{rlibdir}/genoCN/doc
%doc %{rlibdir}/genoCN/html
%{rlibdir}/genoCN/R
%{rlibdir}/genoCN/INDEX
%{rlibdir}/genoCN/help
%{rlibdir}/genoCN/data
%{rlibdir}/genoCN/NAMESPACE
%{rlibdir}/genoCN/libs
%{rlibdir}/genoCN/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora