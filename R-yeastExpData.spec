%global packname  yeastExpData
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.19
Release:          1%{?dist}
Summary:          Yeast Experimental Data

Group:            Applications/Engineering 
License:          GPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph 

BuildRequires:    R-devel tex(latex) R-graph 

%description
A collection of different sets of experimental data from yeast.

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
%doc %{rlibdir}/yeastExpData/doc
%doc %{rlibdir}/yeastExpData/DESCRIPTION
%doc %{rlibdir}/yeastExpData/html
%{rlibdir}/yeastExpData/scripts
%{rlibdir}/yeastExpData/NAMESPACE
%{rlibdir}/yeastExpData/Meta
%{rlibdir}/yeastExpData/data
%{rlibdir}/yeastExpData/help
%{rlibdir}/yeastExpData/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.19-1
- initial package for Fedora