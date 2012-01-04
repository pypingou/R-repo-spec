%global packname  flowFlowJo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Tools for extracting information from a FlowJo workspace and working with the data in the flowCore paradigm.

Group:            Applications/Engineering 
License:          GPL (>=3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 
Requires:         R-flowCore R-XML R-methods R-Biobase 

BuildRequires:    R-devel tex(latex) R-MASS
BuildRequires:    R-flowCore R-XML R-methods R-Biobase 


%description
FlowJo is a commercial GUI based software package from TreeStar Inc. for
the visualization and analysis of flow cytometry data.  One of the FlowJo
standard export file types is the "FlowJo Workspace".  This is an XML
document that describes files and manipulations that have been performed
in the FlowJo GUI environment.  This package can take apart the FlowJo
workspace and deliver the data into R in the flowCore paradigm.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora